from src.Application import blueprint_file
from src.Application.Handler.PostFileHandler import PostFileHandler


@blueprint_file.route("/files", methods=["POST"])
def post_file():
    return PostFileHandler().post()
