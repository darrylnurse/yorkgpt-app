from reset_vectorstore import reset_vectorstore

# this module is simply called by cron (cli - python3) to refresh the vectorstore daily
# the reason i didnt simply call this function in the reset_vectorstore module is so that it wouldnt be called twice on module load
# tldr; efficiency
reset_vectorstore()