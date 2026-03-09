"""LangGraph 图定义（工作流编排）。"""

from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class ExampleState(TypedDict):
    """示例图状态。"""
    messages: list[str]


def _example_node(state: ExampleState) -> ExampleState:
    """示例节点：在 messages 后追加一条。"""
    return {"messages": state.get("messages", []) + ["processed"]}


# 示例：最小状态与图
example_graph_builder = (
    StateGraph(ExampleState)
    .add_node("example", _example_node)
    .add_edge(START, "example")
    .add_edge("example", END)
)

# 编译为可执行图（API 中可注入并 invoke）
example_graph = example_graph_builder.compile()
