import React, { Component } from 'react';
import { Link, NavLink } from 'react-router-dom';
import {
  Badge,
  UncontrolledDropdown,
  DropdownItem,
  DropdownMenu,
  DropdownToggle,
  Nav,
  NavItem,
} from 'reactstrap';
import PropTypes from 'prop-types';

import {
  AppAsideToggler,
  AppNavbarBrand,
  AppSidebarToggler,
} from '@coreui/react';
import logo from '../../assets/img/brand/logo.png';
import sygnet from '../../assets/img/brand/sygnet.svg';

const propTypes = {
  children: PropTypes.node,
};

const defaultProps = {};

const DefaultHeader = (props) => {
  // eslint-disable-next-line
  const { children, ...attributes } = props;

  return (
    <>
      <AppSidebarToggler className="d-lg-none" display="md" mobile />
      <AppNavbarBrand
        className="img-responsive"
        full={{ src: logo, width: 150, alt: 'Harden Clean Logo' }}
        minimized={{
          src: sygnet,
          width: 30,
          height: 30,
          alt: 'CoreUI Logo',
        }}
      />
      <AppSidebarToggler className="d-md-down-none" display="lg" />

      <Nav className="ml-auto" navbar>
        <NavItem className="d-md-down-none">
          <NavLink to="#" className="nav-link">
            <i className="icon-bell" />
            <Badge pill color="danger">
              5
            </Badge>
          </NavLink>
        </NavItem>

        <UncontrolledDropdown nav direction="down">
          <DropdownToggle nav>
            <img
              src="../../assets/img/avatars/6.jpg"
              className="img-avatar"
              alt="admin@bootstrapmaster.com"
            />
          </DropdownToggle>
          <DropdownMenu right>
            <DropdownItem>
              <i className="fa fa-user" />
              Profile
            </DropdownItem>
            <DropdownItem>
              <i className="fa fa-wrench" />
              Settings
            </DropdownItem>
            <DropdownItem onClick={(e) => this.props.onLogout(e)}>
              <i className="fa fa-lock" />
              Logout
            </DropdownItem>
          </DropdownMenu>
        </UncontrolledDropdown>
      </Nav>
      {/* <AppAsideToggler className="d-lg-none" mobile /> */}
    </>
  );
};

DefaultHeader.propTypes = propTypes;
DefaultHeader.defaultProps = defaultProps;

export default DefaultHeader;
