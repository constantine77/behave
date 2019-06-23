from behave import given, when, then, step

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0

@given('Expected Record count for output file')
def step_impl(context):
    for row in context.table:
        input = row["input"]
    context.input_count = int(input.strip())

@then('I will see the record count match input vs output')
def step_impl(context):
    num_lines = 0
    file_name = "/Users/constantine/Applications/Projects/Python/behave/features/output/output.csv"
    with open(file_name,"r") as f:
        for line in f:
            num_lines +=1
    assert(context.input_count == num_lines)