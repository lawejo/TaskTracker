from bottle import default_app, get, post, request, response, run, static_file

import routes.render_index



##############################
##### Så den kan finde vores JS

@get("/js/<filename>")
def _(filename):
    return static_file(filename, "js")

##############################
##### Så den kan finde billeder

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")


@get("/images/<filename:re:.*\.JPG>")
def _(filename):
    return static_file(filename, root="./images")


@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
    return static_file(filename, root="./images")



@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")



@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")

#############################
##### Så den kan finde CSS


@get("/output.css")
def _():
    return static_file("output.css", root=".")


# Import Apis
import apis.api_create_task
import apis.api_delete_task
import apis.api_edit_task


#############################

try:
    import production
    application = default_app()
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=3000, debug=True, reloader=True, )
