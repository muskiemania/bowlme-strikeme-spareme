import React, { Component } from 'react';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import './create.less';

import _ from 'lodash';
import Button from '../button/button';

class Create extends Component {

    render() {

        return (
            <div className='create-game'>
                <div className='grid-x row align-center'>
                    <div className='column'>
                        <input type='text' placeholder='Enter Your Name' />
                    </div>
                </div>
                <div className='grid-x row align-center'>
                    <div className='column'>
                        <Button text='Play Now!' />
                    </div>
                </div>
            </div>
        );
    }
}

export default Create;
