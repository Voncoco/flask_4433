from app import create_app
from app.libs.error import APIException
from werkzeug.exceptions import HTTPException
from app.libs.error_code import ServerError


app = create_app()


# @app.errorhandler(Exception)
def framework_error(e):
    """
    全局异常处理
    """
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if app.config['DEBUG'] is False:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)
