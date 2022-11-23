const GET_SETS = 'sets/get'

const get_sets = (sets) => {
    return {
        type: GET_SETS,
        sets: sets
    }
}


export default function setsReducer(state = initialState, action) {
    switch (action.type) {
        case GET_SETS:

        default:
            return state;
    }
}
