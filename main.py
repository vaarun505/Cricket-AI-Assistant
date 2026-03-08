from analysis.stats import load_data, calculate_stats
from analysis.llm_analysis import generate_analysis, analyze_ball

data = load_data("Data/deliveries.json")
stats = calculate_stats(data)

print("Bowling Session Summary")
print("----------------------")

print(f"Average Speed: {stats['average_speed']} km/h")
print(f"Good Length Deliveries: {stats['good_length']}/{stats['total_balls']}")
print(f"Outside Off Deliveries: {stats['outside_off']}/{stats['total_balls']}")

# ---- Combined AI analysis ----

print("\nAI Coach Overall Analysis")
print("----------------------")

analysis = generate_analysis(stats)

print(analysis)

# ---- Ball by Ball ----

print("\nBall by Ball Analysis")
print("----------------------")

for ball in data:

    print(f"\nBall {ball['ball']}:")

    ball_analysis = analyze_ball(ball)

    print(ball_analysis)