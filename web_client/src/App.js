import React, { Component } from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
// import { renderRoutes } from 'react-router-config';
import { connect } from 'react-redux';
import './App.scss';

const loading = () => <div className="animated fadeIn pt-3 text-center"> Loading... </div>;

// Containers
const DefaultLayout = React.lazy(() => import('./containers/DefaultLayout'));
const ProtectedRoute = React.lazy(() => import('./containers/ProtectedRoute'));

// Pages
const Login = React.lazy(() => import('./views/Pages/Login'));
const Register = React.lazy(() => import('./views/Pages/Register'));
const Page404 = React.lazy(() => import('./views/Pages/Page404'));
const Page500 = React.lazy(() => import('./views/Pages/Page500'));

class App extends Component {
	render() {
		const { isAuthenticated, isVerifying } = this.props;
		return (
			<HashRouter>
				<React.Suspense fallback={loading()}>
					<Switch>
						<Route exact path="/login" name="Login Page" render={(props) => <Login {...props} />} />
						<Route
							exact
							path="/register"
							name="Register Page"
							render={(props) => <Register {...props} />}
						/>
						<Route exact path="/404" name="Page 404" render={(props) => <Page404 {...props} />} />
						<Route exact path="/500" name="Page 500" render={(props) => <Page500 {...props} />} />
						{/* <Route path="/" name="Home" render={(props) => <DefaultLayout {...props} />} /> */}
						<ProtectedRoute
							exact
							path="/"
							render={(props) => <DefaultLayout {...props} />}
							isAuthenticated={isAuthenticated}
							isVerifying={isVerifying}
							name="Home"
						/>
					</Switch>{' '}
				</React.Suspense>{' '}
			</HashRouter>
		);
	}
}

const mapStateToProps = (state) => {
	return {
		isAuthenticated: state.auth.isAuthenticated,
		isVerifying: state.auth.isVerifying
	};
};
export default connect(mapStateToProps)(App);
