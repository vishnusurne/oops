def student_upper(fun):
    def inner():
        result=fun()
        return result.upper()
    return inner

@student_upper
def student_fullname():
    fn=input("name:")
    mn=input("Mname:")
    ln=input("Lname:")
    return f'{fn} {mn} {ln}'
print(student_fullname())