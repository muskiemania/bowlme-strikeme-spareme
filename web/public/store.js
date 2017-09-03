import { createStore } from 'redux';
import counterApp from './reducers';

let store = createStore(counterApp);

export default store;
