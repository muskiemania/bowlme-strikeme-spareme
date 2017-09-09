import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {CounterActions} from './actions';

class AnotherComponent extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <h2>This is another component</h2>
            </div>
        )
    }
}

export default AnotherComponent;
    

    
