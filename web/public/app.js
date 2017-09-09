import React from 'react'
import { render } from 'react-dom'
import Counter from './counter'
import { Provider } from 'react-redux'
import { createStore, combineReducers } from 'redux'
import counterApp from './reducers'
import { Router, Route, browserHistory, IndexRoute} from 'react-router'
import { syncHistoryWithStore, routerReducer } from 'react-router-redux'
import MainComponent from './mainComponent'
import AnotherComponent from './anotherComponent'
import PokerTable from './components/shared/pokerTable/pokerTable'
import TableContainer from './components/shared/containers/tableContainer'

import Welcome from './components/welcome/welcome'

const store = createStore(combineReducers({global: counterApp, routing: routerReducer}));

const history = syncHistoryWithStore(browserHistory, store);

render(
    <Provider store={store}>
        <TableContainer>
            <Router history={history}>
                <Route path='/' component={Welcome} />
                <Route path='/test' component={PokerTable} />
            </Router>
        </TableContainer>
    </Provider>,
    document.getElementById("app")
)
