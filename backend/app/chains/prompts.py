"""LangChain PromptTemplate 定义。"""

from langchain_core.prompts import PromptTemplate

# 示例：短剧剧情摘要
example_prompt = PromptTemplate(
    input_variables=["script_text"],
    template="请对以下短剧剧本做简要摘要，突出人物与情节要点：\n\n{script_text}",
)

# 可在此扩展更多模板，供 Agent / 工作流使用
STORY_SUMMARY_TEMPLATE = PromptTemplate(
    input_variables=["script_text"],
    template="请对以下短剧剧本做简要摘要，突出人物与情节要点：\n\n{script_text}",
)
