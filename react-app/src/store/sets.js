const GET_SETS = 'sets/get'

const getSets = (sets) => {
    return {
        type: GET_SETS,
        sets: sets.sets
    }
}

export const getFeaturedSetsThunk = () => async (dispatch) => {
    const response = await fetch('/api/sets/featured')

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(getSets(data));
    }
}

export const getSessionSetsThunk = () => async (dispatch) => {
    const response = await fetch('/api/sets/session')

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(getSets(data));
    }
}

export const getOneSetThunk = (id) => async (dispatch) => {
    const response = await fetch(`/api/sets/${id}`)

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(getSets(data));
        return true
    } else return false
}

const CLEAR_SETS = "/sets/clear/all"

export const clearSets = () => {
    return {
        type: CLEAR_SETS
    }
}

export default function setsReducer(state = null, action) {
    switch (action.type) {
        case GET_SETS:
            let getSetsState = {}
            for (let i = 0; i < action.sets.length; i++) {
                getSetsState[action.sets[i].id] = action.sets[i]
            }
            return getSetsState
        case CLEAR_SETS:
            return null
        default:
            return state;
    }
}
