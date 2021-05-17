from behave import given, when, then


@given('I open Google')
def step_impl(context):
    context.google.open()
    assert context.google.get_page_title().__contains__('Google')


@given('I want to get info about a {name} song')
def step_impl(context, name):
    context.google.search(name + ' wiki')


@when('I open Wikipedia')
def step_impl(context):
    context.google.open_wikipedia()


@then('Song producer is {group}')
def step_impl(context, group):
    assert context.wikipedia.get_song_author() == group


@then('Release year is {release_year}')
def step_impl(context, release_year):
    assert context.wikipedia.get_song_release_year() == release_year
