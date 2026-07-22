from langchain_deepseek import ChatDeepSeek
from schemas.agent import NameResultSchema, NameSchema
from schemas.name import NameIn
import json
import re

llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key="sk-4872aa4002c94935b5a4f5f9ae0ac4b7",
    temperature=1,
)

system_prompt = """
你是起名大师,一位精通汉语言文学、音韵学与传统文化的命名专家，擅长为人物创作兼具音律美感、深刻寓意与文化内涵的姓名。请严格遵循以下原则进行命名：
发音优先：名字需平仄协调、声调起伏自然，避免拗口、谐音歧义（如不雅谐音、负面联想），朗朗上口，富有韵律感；
寓意深远：结合用户提供的背景（如姓氏、性别、字数和其他要求等），选取具有积极象征意义的意象（如自然元素、美德品质、经典典故），做到“名以载道”；
内涵厚重：优先从《诗经》《楚辞》《论语》等经典文献，或唐诗宋词、成语典故中汲取灵感，确保名字有出处、有底蕴，避免空洞堆砌；
现代适配：在尊重传统的基础上，兼顾当代语境与审美，避免过度古奥或生僻字（生僻字需附注音与释义），确保实用性与传播性；
两字的意思是除了姓氏2个字的名字总长为3个字，单字是除了姓氏1个字的名字总长为2个字，不限的意思是你需要50%概率生成两字，50%概率生成单字
个性化定制：根据用户具体需求（如性别倾向、字数限制、风格偏好——儒雅/清丽/大气/灵动等），提供5个候选方案，并按照以下格式输出：
【姓名】姓名
【出处】典籍来源或文化意象
【寓意】字义拆解与整体象征
只返回标准JSON，不要多余内容！
格式：
{
    "names": [
        {"name":"名字", "reference":"出处", "moral":"寓意"}
    ]
}
返回5个！
"""

async def generate_names(name_info: NameIn) -> NameResultSchema:
    prompt = f"""
{system_prompt}
用户需求：
姓氏：{name_info.surname}
性别：{name_info.gender}
字数：{name_info.length}
其他要求：{name_info.other}
排除：{"、".join(name_info.exclude)}
"""

    response = await llm.ainvoke(prompt)
    content = response.content

    try:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        data = json.loads(match.group(0)) if match else {"names": []}
    except:
        data = {"names": []}

    names = [NameSchema(**n) for n in data.get("names", [])[:5]]
    return NameResultSchema(names=names)