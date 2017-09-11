export const ITEMS_HAS_ERRORED = 'ITEMS_HAS_ERRORED'
export const ITEMS_IS_LOADING = 'ITEMS_IS_LOADING'
export const ITEMS_FETCH_DATA_SUCCESS = 'ITEMS_FETCH_DATA_SUCCESS'

export function isError(bool) {
    return {
        type: ITEMS_HAS_ERRORED,
        isErrored: bool
    };
}

export function isLoading(bool) {
    return {
        type: ITEMS_IS_LOADING,
        isLoading: bool
    };
}

export function fetchDataSuccess(data) {

    let cards = data['cards'];
    
    return {
        type: ITEMS_FETCH_DATA_SUCCESS,
        cards
    };
}

export function pokerGameFetchData(url) {
    return (dispatch) => {
        dispatch(isLoading(true));
        
        fetch(url)
            .then((response) => {

                if (!response.ok) {
                    throw Error(response.statusText);
                }
                
                dispatch(isLoading(false));

                return response;
            })
            .then((response) => response.json())
            .then((data) => dispatch(fetchDataSuccess(data)))
            .catch((e) => {
                dispatch(isError(true))
            });
    };
}
