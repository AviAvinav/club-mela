from django.shortcuts import render
from django.db import connection

# Create your views here.
def main(request):
    password = ''
    message = ''
    
    if request.method == 'GET' and 'password' in request.GET:
        password = request.GET['password']
        print(f"WHERE password = '{password}'")
        with connection.cursor() as cursor:
            query = f"SELECT password FROM guess_admin WHERE guess_admin.password = '{password}'"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)

        if result:
            message = "Correct password! The password is: " + result[0][0]
        else:
            message = "Incorrect password!"

    return render(request, 'index.html', {'message': message})#mitigates js requirements for dynamic loading
