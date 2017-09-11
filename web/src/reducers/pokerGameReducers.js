import Immutable from 'immutable';

export function isError(state = false, action) {
    switch(action.type) {
        case 'ITEMS_HAS_ERRORED':
            return action.isError;
        default:
            return state;
    }
}

export function isLoading(state = false, action) {
    switch(action.type) {
        case 'ITEMS_IS_LOADING':
            return action.isLoading;
        default:
            return state;
    }
}

export function cards(state = Immutable.List(), action) {
    switch(action.type) {
        case 'ITEMS_FETCH_DATA_SUCCESS':
            return Immutable.fromJS(action.cards);
        default:
            return state;
    }
}
