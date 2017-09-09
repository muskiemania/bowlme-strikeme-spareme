import { combineReducers } from 'redux';
import { cards, itemsHasErrored, itemsIsLoading } from './pokerGameReducers';

export default combineReducers({
    cards,
    itemsHasErrored,
    itemsIsLoading
});
