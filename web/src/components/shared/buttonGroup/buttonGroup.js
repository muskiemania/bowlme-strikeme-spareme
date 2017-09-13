import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './buttonGroup.less';

class ButtonGroup extends Component {

    render() {
        return (
            <ul className='button-group draw-button-group'>
                {
                    this.props.children.length ? this.props.children.map((child, i) => {
                        return (<li key={`button-${i}`}>{child}</li>);
                    }) : <li>{this.props.children}</li>
                }
            </ul>
        );
    }
}

export default ButtonGroup;
