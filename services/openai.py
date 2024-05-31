import numpy as np
import pandas as pd
from openai import AsyncOpenAI
from typing import List

from common.constants.common import CONTENT, ROLE, SYSTEM, USER, EMBEDDING, SIMILARITY
from common.constants.file_name import EMBEDDING_CSV_FILE
from common.types.search_result import SearchResult
from config.dot_env import OPENAI_API_KEY, CHAT_MODEL, EMBEDDING_MODEL


class OpenaiService:

    def __init__(self) -> None:
        self.client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    async def search_embedding(self, prompt: str = None, top_head: int = 3, file_path: str = EMBEDDING_CSV_FILE) -> list[SearchResult]:
        df = pd.read_csv(file_path)
        df[EMBEDDING] = df.embedding.apply(eval).apply(np.array)
        prompt_embedding = await self.get_embedding(text=prompt, model=EMBEDDING_MODEL)
        df[SIMILARITY] = df.embedding.apply(lambda x: self.__cosine_similarity(x, prompt_embedding))
        result = df.sort_values(SIMILARITY, ascending=False).head(top_head)
        return [SearchResult(answer=result.combined.iloc[num]) for num in range(3)]

    async def chat_completion(self, prompt: str, message: str = None, history: list[dict] = []) -> str:
        messages = [{ROLE: SYSTEM, CONTENT: prompt}] + history + [{ROLE: USER, CONTENT: message}]
        completions = await self.client.chat.completions.create(
            model=CHAT_MODEL,
            messages=messages,
            temperature=0.7,
        )
        response = completions.choices[0].message.content
        return response

    async def get_embedding(self, text: str, model: str) -> List[float]:
        embedding = (await self.client.embeddings.create(input=text, model=model)).data[0].embedding
        return embedding

    def __cosine_similarity(self, vector_a: List[float], vector_b: List[float]) -> float:
        return np.dot(vector_a, vector_b) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))
