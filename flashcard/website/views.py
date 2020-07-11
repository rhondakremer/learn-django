from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {}) # context dictionary

def add(request):
    from random import randint
    num_1 = randint(0, 9)
    num_2 = randint(0, 9)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # error handling if no answer submitted
        if not answer: 
            my_answer = "Please enter a valid number."
            color = 'warning'
            return render(request, 'add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
        })

        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + str(correct_answer)
            color = "success"
        else:
            my_answer = "Wrong :( " + old_num_1 + " + " + old_num_2 + " does not equal " + answer
            color = "danger"
        return render(request, 'add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })

    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2,
    })

def subtract(request):
    from random import randint
    num_1 = randint(0, 9)
    num_2 = randint(0, 9)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # error handling if no answer submitted
        if not answer: 
            my_answer = "Please enter a valid number."
            color = 'warning'
            return render(request, 'subtract.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
        })

        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " - " + old_num_2 + " = " + str(correct_answer)
            color = "success"
        else:
            my_answer = "Wrong :( " + old_num_1 + " - " + old_num_2 + " does not equal " + answer
            color = "danger"
        return render(request, 'subtract.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })

    return render(request, 'subtract.html', {
        'num_1': num_1,
        'num_2': num_2,
    })

def multiply(request):
    from random import randint
    num_1 = randint(0, 9)
    num_2 = randint(0, 9)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # error handling if no answer submitted
        if not answer: 
            my_answer = "Please enter a valid number."
            color = 'warning'
            return render(request, 'multiply.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
        })

        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " * " + old_num_2 + " = " + str(correct_answer)
            color = "success"
        else:
            my_answer = "Wrong :( " + old_num_1 + " * " + old_num_2 + " does not equal " + answer
            color = "danger"
        return render(request, 'multiply.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })

    return render(request, 'multiply.html', {
        'num_1': num_1,
        'num_2': num_2,
    })

def divide(request):
    from random import randint
    num_1 = randint(0, 9)
    num_2 = randint(1, 9)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # error handling if no answer submitted
        if not answer: 
            my_answer = "Please enter a valid number."
            color = 'warning'
            return render(request, 'divide.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
        })

        correct_answer = round(int(old_num_1) / int(old_num_2), 2)
        if float(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " / " + old_num_2 + " = " + str(correct_answer)
            color = "success"
        else:
            my_answer = "Wrong :( " + old_num_1 + " / " + old_num_2 + " does not equal " + answer + "it equals " + str(correct_answer),
            color = "danger"
        return render(request, 'divide.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })

    return render(request, 'divide.html', {
        'num_1': num_1,
        'num_2': num_2,
    })
