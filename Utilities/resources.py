class ApiResources:
    default_value = 2
    delayValue = 3

    # GET API REQUESTS
    getAllUsersList = f'api/user?page={default_value}'
    getSingleUserList = f'api/user/{default_value}'
    getUserNotFoundList = f'api/user/{default_value}'  # use parameter 23 for it

    getAllUnknownUsersList = f'api/unknown'
    getSingleUnknownUserList = f'api/unknown/{default_value}'
    getSingleUserNotFoundList = f'api/unknown/{default_value}'  # use parameter 23 for it

    getDelayResp = f'api/user?delay={delayValue}'

    # POST API REQUESTS
    createUser = 'api/users'
    registerUserSuccessful = 'api/register'
    registerUserUnsuccessful = 'api/register'
    loginUserSuccessful = 'api/login'
    loginUserUnsuccessful = 'api/login'

    # PUT API REQUESTS
    updateUser = f'api/users/{default_value}'

    # PATCH API REQUESTS
    patchUpdateUser = f'api/users/{default_value}'

    # DELETE API REQUESTS
    deleteUser = f'api/users/{default_value}'
