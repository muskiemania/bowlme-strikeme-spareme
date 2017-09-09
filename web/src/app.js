import React from 'react'
import { render } from 'react-dom'
import configureStore from './store/configureStore'
import Root from './components/root/root'

const store = configureStore();

render(
    <Root store={store} />,
    document.getElementById("app")
)
