def main():
    N = int(input())
    plan = [tuple(map(int, input().split())) for _ in range(N)]

    print(is_possible_travel_plan(plan))

def is_possible_travel_plan(plan):
    t0 = 0
    x0 = 0
    y0 = 0

    for t, x, y in plan:
        distance = abs(x - x0) + abs(y - y0)
        time_diff = t - t0

        # 距離条件と条件を確認
        if distance > time_diff or (distance % 2 != time_diff % 2):
            return "No"

        # 現在地更新
        t0, x0, y0 = t, x, y

    return "Yes"

if __name__ == "__main__":
    main()