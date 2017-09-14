import React, { Component } from 'react';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import _ from 'lodash';
import Button from '../shared/button/button';

import Join from '../shared/join/join';
import Create from '../shared/create/create';
import Welcome from '../shared/welcome/welcome';



class JoinCreate extends Component {

    constructor(props) {
        super(props);

        this.state = { mode: 'welcome' };
    }

    clickSetModeCreate() {
        this.setState({ mode: 'create' });
    }

    clickSetModeJoin() {
        this.setState({ mode: 'join' });
    }

    factory() {
        switch(this.state.mode) {
            case 'create':
                return (<Create />);
            case 'join':
                return (<Join />);
            default:
                return (<Welcome clickCreate={this.clickSetModeCreate.bind(this)} clickJoin={this.clickSetModeJoin.bind(this)} />);
        }
    }

    render() {
        return (
            <div className='join-create'>
                {
                    this.factory()
                }
            </div>
        );
    }
}

export default JoinCreate;
