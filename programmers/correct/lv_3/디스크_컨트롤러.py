import heapq

def solution(jobs):
    answer = 0
    job_dict = {} # job 딕셔너리 (요청 시점 : [소요 시간1, 소요시간2, ...])
    wait_jobs = [] # 현재 시점에서 대기중인 job
    remain_time = 0 # 현재 수행중인 job의 남은 소요 시간
    is_busy = False # 현재 하드디스크 상태

    # job 딕셔너리로 포맷팅 (jobs가 요청 시점 순 정렬이 안되어 있을수도 있고, 같은 요청 시점에 job이 여러개일 수 있으므로 이런 형태가 낫다고 판단)
    for job in jobs:
        if job[0] in job_dict:
            job_dict[job[0]].append(job[1])
        else:
            job_dict[job[0]] = [job[1]]

    for time in range(1000 * 1000): # 요청 시점 최대값과 소요시간 최대값이 각각 1000이므로 최악의 경우까지 생각
        # time은 현재 시각
        if remain_time == 0:
            is_busy = False
        else:
            is_busy = True

        if time in job_dict: # 현재 시각과 요청 시점이 일치하는 job들 대기열에 넣기 (소요시간이 짧을수록 우선순위 높음)
            for j in job_dict[time]:
                heapq.heappush(wait_jobs, (j, time))

        if is_busy: # 하드디스크 작업 중
            remain_time -= 1
        else: # 하드디스크 노는 중
            if wait_jobs: # 대기 job이 있으면
                need_time, req_time = heapq.heappop(wait_jobs)
                remain_time = need_time - 1
                answer += (time - req_time) + need_time # 작업 시간 더하기. 평균 작업시간을 구하기 위함
                is_busy = True

    return int(answer / len(jobs))

"""
1. 어쨌든 모든 job들을 완료하기 위한 총 시간은 같다?
2. 대기열에 여러 job이 있을때 무얼먼저 선택하던 job들의 총 대기시간의 합은 같다?
    - ㄴㄴ 소요시간이 짧은 job을 선택할수록 다른 job들의 대기시간이 짧아짐
"""