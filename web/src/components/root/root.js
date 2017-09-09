import React from 'react'
import PropTypes from 'prop-types'
import { Provider } from 'react-redux'
import { Router, Route, browserHistory, IndexRoute} from 'react-router'

import PokerHand from '../pokerHand/pokerHand'

const Root = ({ store }) => (
    <div className={'poker-table'}>
        <Provider store={store}>
            <Router history={browserHistory}>
                <Route path="/(:filter)" component={PokerHand} />
            </Router>
        </Provider>
    </div>
)

Root.propTypes = {
    store: PropTypes.object.isRequired
}

export default Root
