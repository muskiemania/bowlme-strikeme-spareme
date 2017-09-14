import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Immutable from 'immutable';

import _ from 'lodash';
import Button from '../button/button';
import './welcome.less';

class Welcome extends Component {

    render() {

        let {clickCreate, clickJoin} = this.props;
        
        return (
            <div className='welcome'>
                <div className='grid-x row align-center'>
                    <div className='column'>
                        <Button text='Create Game' click={clickCreate} />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                        <Button text='Join Game' click={clickJoin} />
                    </div>
                </div>
            </div>
        );
    }
}

Welcome.PropTypes = {
    clickCreate: PropTypes.func,
    clickJoin: PropTypes.func
};

export default Welcome;
