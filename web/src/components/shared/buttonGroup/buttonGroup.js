import React, { Component } from 'react';
import PropTypes from 'prop-types';
import classname from 'classnames';
import './buttonGroup.less';

class ButtonGroup extends Component {

    render() {

	let {stack} = this.props;

        return (
		<ul className={classname('button-group','draw-button-group', stack ? 'stacked' : '')}>
                {
                    this.props.children.length ? this.props.children.map((child, i) => {
                        return (<li key={`button-${i}`}>{child}</li>);
                    }) : <li>{this.props.children}</li>
                }
            </ul>
        );
    }
}

ButtonGroup.PropTypes = {
    stack: PropTypes.bool
}

export default ButtonGroup;
