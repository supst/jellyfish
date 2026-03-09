"""示例路由：演示 PromptTemplate 与 LangGraph。"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.chains.prompts import example_prompt
from app.chains.graphs import example_graph

router = APIRouter()


class GraphRequest(BaseModel):
    """LangGraph 示例请求体。"""
    messages: list[str] | None = None


@router.get("/prompt")
async def get_prompt_example():
    """返回 PromptTemplate 格式化示例（不调用 LLM）。"""
    formatted = example_prompt.format(script_text="第一场：小明走进教室...")
    return {"formatted_prompt": formatted}


@router.post("/graph")
async def run_example_graph(body: GraphRequest):
    """运行示例 LangGraph，返回新状态。"""
    messages = body.messages or ["hello"]
    initial = {"messages": messages}
    result = await example_graph.ainvoke(initial)
    return {"state": result}
