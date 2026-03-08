from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)


session_prompt = PromptTemplate(
    input_variables=["avg_speed","good_length","outside_off","total"],
    template="""
You are an elite cricket bowling coach.

Analyze the bowling session stats.

Average speed: {avg_speed} km/h
Good length deliveries: {good_length}/{total}
Outside off deliveries: {outside_off}/{total}

Provide:
1. Overall assessment
2. Strengths
3. Areas for improvement
"""
)

session_chain = session_prompt | llm


def generate_analysis(stats):

    result = session_chain.invoke({
        "avg_speed": stats["average_speed"],
        "good_length": stats["good_length"],
        "outside_off": stats["outside_off"],
        "total": stats["total_balls"]
    })

    return result.content


# ----- BALL ANALYSIS -----

ball_prompt = PromptTemplate(
    input_variables=["ball","speed","line","length","swing"],
    template="""
You are a cricket coach.

Analyze this delivery:

Ball number: {ball}
Speed: {speed} km/h
Line: {line}
Length: {length}
Swing: {swing}

Give a short coaching commentary.
"""
)

ball_chain = ball_prompt | llm


def analyze_ball(ball_data):

    result = ball_chain.invoke({
        "ball": ball_data["ball"],
        "speed": ball_data["speed"],
        "line": ball_data["line"],
        "length": ball_data["length"],
        "swing": ball_data["swing"]
    })

    return result.content