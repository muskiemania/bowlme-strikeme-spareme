import React, { Component } from 'react';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './join.less';

import _ from 'lodash';
import Button from '../button/button';

class Join extends Component {

    render() {

        return (
            <div className='join-game'>
                <div className='grid-x row align-center'>
                    <div className='column'>
                        <input type='text' placeholder='Enter Your Name' />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                        <input type='text' placeholder='Enter Game ID' />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                        <Button text='Join Game Now' />
                    </div>
                </div>
            </div>
        );
    }
}

export default Join;
