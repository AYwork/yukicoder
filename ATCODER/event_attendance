def main():
    event_period = int(input())
    number_of_participants = int(input())
    attendee_list = [0] * (event_period+1) #開催日ごとのリストを用意

    for i in range(number_of_participants):
        first_day, last_day = map(int, input().split())
        attendee_list[first_day-1] += 1
        attendee_list[last_day] -= 1

    answer = 0
    for attendees_of_the_day in attendee_list[:-1]:
        answer += attendees_of_the_day
        print(answer)



if __name__ == "__main__":
    main()