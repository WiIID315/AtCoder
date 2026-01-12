n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
v.append(0)

target_v = [0] * (n + 1)

for i in range(n - 1, 0, -1):
    target_v[i] = min(v[i-1], v[i], target_v[i+1] + t[i])

total_area = 0
curr_v = 0
"""
	A few cases to consider:
	Trapezoid: Next v is lower than the max v you can reach
	Flat: Next v is the same
	Not Enough Time: You can't reach max v before reaching the next one: i.e. you have a triangle for that 't'
"""
for i in range(n):
	cap = v[i]
	end = target_v[i + 1]
	time = t[i]
	# print("Moving at: ", curr_v, "with", total_area, "accumulated")
	if(end - curr_v >= time):
		total_area += curr_v * time + (time * time) / 2
		curr_v += time
	elif cap == end:
		# print("Flat case:", curr_v * time + (cap - curr_v) * (cap - curr_v) / 2 + cap * (time - (cap - curr_v)))
		total_area += curr_v * time
		total_area += (cap - curr_v) * (cap - curr_v) / 2 + (cap - curr_v) * (time - (cap - curr_v))
		curr_v = end
	else:
		#O(t) scan: Find a fixed point j where you stop increasing speed, 
		# see if it's possible to lower back down to end and find the largest area out of these
		best_area = 0
		for k in range(max(0, end - curr_v) * 2, time * 2):
			j = k / 2
			time_to_slow = curr_v + j - end
			if j + curr_v > cap or j + time_to_slow > time:
				break
			temp_area = 0
			temp_area += curr_v * (time - time_to_slow) + end * time_to_slow
			temp_area += j * j / 2 + time_to_slow * time_to_slow / 2
			temp_area += (time - time_to_slow - j) * j
			# print(j, temp_area)
			best_area = max(best_area, temp_area)
		total_area += best_area
		curr_v = end
#nprint("Moving at: ", curr_v, "with", total_area, "accumulated")

print(total_area)