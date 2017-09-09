import React from 'react'
import PropTypes from 'prop-types'

class Welcome extends React.Component {

    render() {
        let {message} = this.props;
        return (
            <div>
                <div>{message || 'hi there'}</div>
            
                <form action="create" method="POST">
                    <input type="submit" value="Create a new game" />
                </form>
            </div>
        )
    }
}

Welcome.propTypes = {
    message: PropTypes.string
}

export default Welcome
