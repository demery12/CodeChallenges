def text_transpose(text):
	longest = 0
	line_list=[]
	line = []
	for char in text:
		if char == '\n':
			line_list += [line]
			if len(line)>longest:
				longest = len(line)
			line = []
		else:
			line += [char]
	if len(line)>longest:
		longest = len(line)
	line_list += [line]
	index = 0
	for line in line_list:
		if len(line)<longest:
			line_list[index] = line + (longest-len(line))*[' ']
		index += 1
	#now I pretty much have a matrix and could/would use numpy
	n = len(line_list)
	m = len(line_list[0])
	transpose_line = []
	transpose = []
	i = 0
	while i < m:
		for line in line_list:
			transpose_line += [line[i]]
		transpose += [transpose_line]
		transpose_line =[]
		i+=1
	print transpose
	print line_list
	print text
text_transpose("a b c\nd e f")
text_transpose("Some\ntext.")

a = """package main

import "fmt"

func main() {
    queue := make(chan string, 2)
    queue <- "one"
    queue <- "twoO"
    close(queue)
    for elem := range queue {
        fmt.Println(elem)
    }
}"""
text_transpose(a)