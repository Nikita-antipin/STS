def get_processed_subs():
    file_with_subs = open(r"C:\Users\Никита\PycharmProjects\pythonProject\dj.txt")
    lines_from_file_with_subs = file_with_subs.readlines()
    check = 0
    size_of_lines_from_file_with_subs = len(lines_from_file_with_subs)
    times_of_lines = []
    text_of_lines = []

    def get_from_line_amount_of_sec(line):
        hours = int(line[0:2])
        mins = int(line[3:5])
        secs = int(line[6:8])
        secs += float(line[9:12])/1000 + 3600 * hours + 60 * mins
        return secs

    for i in range(size_of_lines_from_file_with_subs):
        if check == 2:
            text_of_lines[len(times_of_lines)-1] +=" " + lines_from_file_with_subs[i][0:(len(lines_from_file_with_subs[i])-1)]
            check = 0
            if i != len(lines_from_file_with_subs)-1:
                if lines_from_file_with_subs[i+1] != "\n":
                    check = 2
        if check == 1:
            check = 0
            text_of_lines += [lines_from_file_with_subs[i][0:(len(lines_from_file_with_subs[i])-1)]]
            if i != len(lines_from_file_with_subs)-1:
                if lines_from_file_with_subs[i+1] != "\n":
                    check = 2
        if lines_from_file_with_subs[i].find("-->") != -1:
            check = 1
            secs = get_from_line_amount_of_sec(lines_from_file_with_subs[i])
            times_of_lines += [secs]
    time_with_text = list(zip(times_of_lines, text_of_lines))
    return time_with_text
