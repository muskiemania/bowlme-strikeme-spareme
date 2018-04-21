import React, { Component } from 'react';

import Immutable from 'immutable';
import ImmutablePropTypes from 'react-immutable-proptypes';

import _ from 'lodash';
import Promise from 'bluebird';

import Button from '../shared/button/button';
import Join from '../shared/join/join';
import Create from '../shared/create/create';
import Welcome from '../shared/welcome/welcome';

import { post, postAnonymous, get } from '../../helpers/http';
import { getApiPath, getWebPath } from '../../helpers/env';

import './joinCreate.less';

class JoinCreate extends Component {

  constructor(props) {
    super(props);

    this.state = { mode: 'welcome' };
  }

  clickSetModeCreate() {
    get(getApiPath() + '/api/game/create')
      .then((respJson) => {
        if (respJson.gameId === 0) {
          this.setState({ mode: 'create' });
        }
        else if (respJson.gameId > 0) {
          window.location.replace(getWebPath() + '/game/');
        }
        else {
          throw 'Unable to determine game';
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }

  clickSetModeJoin() {
    get(getApiPath() + '/api/game/join')
      .then((respJson) => {
        if (respJson.gameId === 0) {
          this.setState({ mode: 'join' });
        }
        else if (respJson.gameId > 0) {
          console.log('why am i redirecting??');
          console.log(respJson.gameId);
          window.location.replace(getWebPath() + '/game/');
        }
        else {
          throw 'Unable to determine game';
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }

  clickCreateGame(playerName) {
    console.log('inside joinCreate.js clickCreateGame');
    postAnonymous(getApiPath() + '/api/game/create', { 'playerName': playerName })
      .then((respJson) => {
        console.log('inside then');
        if (respJson.gameId === 0) {
          throw 'Could not create game';
        }

        window.location.replace(getWebPath() + '/game/');
      })
      .catch((err) => {
        //animation to show error message
        console.log(err);
      });
  }

  clickJoinGame(gameKey, playerName) {
    postAnonymous(getApiPath() + '/api/game/join', { 'gameKey': gameKey, 'playerName': playerName })
      .then((resp) => {
        if (resp.gameId === 0) {
          throw 'Could not create game';
        }

        window.location.replace(getWebPath() + '/game/');
      })
      .catch((err) => {
        //animation to show error message
      });
  }

  factory() {
    switch (this.state.mode) {
      case 'create':
        return (<Create clickCreate={this.clickCreateGame.bind(this)} />);
      case 'join':
        return (<Join clickJoin={this.clickJoinGame.bind(this)} />);
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
