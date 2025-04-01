import React from 'react'

function Navbar() {
  return (
   <>
   <header className="top-header">        
        <nav className="navbar navbar-expand gap-3">
          <div className="mobile-toggle-icon fs-3">
              <i className="bi bi-list"></i>
            </div>
            <form className="searchbar">
                <div className="position-absolute top-50 translate-middle-y search-icon ms-3"><i className="bi bi-search"></i></div>
                <input className="form-control" type="text" placeholder="Type here to search" />
                <div className="position-absolute top-50 translate-middle-y search-close-icon"><i className="bi bi-x-lg"></i></div>
            </form>
            <div className="top-navbar-right ms-auto">
              <ul className="navbar-nav align-items-center">
                <li className="nav-item search-toggle-icon">
                  <a className="nav-link" href="#">
                    <div className="">
                      <i className="bi bi-search"></i>
                    </div>
                  </a>
              </li>
              <li className="nav-item dropdown dropdown-large">
                <a className="nav-link dropdown-toggle dropdown-toggle-nocaret" href="#" data-bs-toggle="dropdown">
                  <div className="projects">
                    <i className="bi bi-grid-3x3-gap-fill"></i>
                  </div>
                </a>
                <div className="dropdown-menu dropdown-menu-end">
                   <div className="row row-cols-3 gx-2">
                      <div className="col">
                        <a href="ecommerce-orders.html">
                         <div className="apps p-2 radius-10 text-center">
                            <div className="apps-icon-box mb-1 text-white bg-gradient-purple">
                              <i className="bi bi-basket2-fill"></i>
                            </div>
                            <p className="mb-0 apps-name">Orders</p>
                         </div>
                        </a>
                      </div>
                      <div className="col">
                        <a href="javascript:;">
                        <div className="apps p-2 radius-10 text-center">
                           <div className="apps-icon-box mb-1 text-white bg-gradient-info">
                            <i className="bi bi-people-fill"></i>
                           </div>
                           <p className="mb-0 apps-name">Users</p>
                        </div>
                      </a>
                     </div>
                     <div className="col">
                      <a href="ecommerce-products-grid.html">
                      <div className="apps p-2 radius-10 text-center">
                         <div className="apps-icon-box mb-1 text-white bg-gradient-success">
                          <i className="bi bi-trophy-fill"></i>
                         </div>
                         <p className="mb-0 apps-name">Products</p>
                      </div>
                      </a>
                    </div>
                    <div className="col">
                      <a href="component-media-object.html">
                      <div className="apps p-2 radius-10 text-center">
                         <div className="apps-icon-box mb-1 text-white bg-gradient-danger">
                          <i className="bi bi-collection-play-fill"></i>
                         </div>
                         <p className="mb-0 apps-name">Media</p>
                      </div>
                      </a>
                    </div>
                    <div className="col">
                      <a href="pages-user-profile.html">
                      <div className="apps p-2 radius-10 text-center">
                         <div className="apps-icon-box mb-1 text-white bg-gradient-warning">
                          <i className="bi bi-person-circle"></i>
                         </div>
                         <p className="mb-0 apps-name">Account</p>
                       </div>
                      </a>
                    </div>
                    <div className="col">
                      <a href="javascript:;">
                      <div className="apps p-2 radius-10 text-center">
                         <div className="apps-icon-box mb-1 text-white bg-gradient-voilet">
                          <i className="bi bi-file-earmark-text-fill"></i>
                         </div>
                         <p className="mb-0 apps-name">Docs</p>
                      </div>
                      </a>
                    </div>
                    <div className="col">
                      <a href="ecommerce-orders-detail.html">
                      <div className="apps p-2 radius-10 text-center">
                         <div className="apps-icon-box mb-1 text-white bg-gradient-branding">
                          <i className="bi bi-credit-card-fill"></i>
                         </div>
                         <p className="mb-0 apps-name">Payment</p>
                      </div>
                      </a>
                    </div>
                    <div className="col">
                      <a href="javascript:;">
                      <div className="apps p-2 radius-10 text-center">
                         <div className="apps-icon-box mb-1 text-white bg-gradient-desert">
                          <i className="bi bi-calendar-check-fill"></i>
                         </div>
                         <p className="mb-0 apps-name">Events</p>
                      </div>
                    </a>
                    </div>
                    <div className="col">
                      <a href="javascript:;">
                      <div className="apps p-2 radius-10 text-center">
                         <div className="apps-icon-box mb-1 text-white bg-gradient-amour">
                          <i className="bi bi-book-half"></i>
                         </div>
                         <p className="mb-0 apps-name">Story</p>
                        </div>
                      </a>
                    </div>
                   </div>
                </div>
              </li>
              <li className="nav-item dropdown dropdown-large">
                <a className="nav-link dropdown-toggle dropdown-toggle-nocaret" href="#" data-bs-toggle="dropdown">
                  <div className="messages">
                    <span className="notify-badge">5</span>
                    <i className="bi bi-chat-right-fill"></i>
                  </div>
                </a>
                <div className="dropdown-menu dropdown-menu-end p-0">
                  <div className="p-2 border-bottom m-2">
                      <h5 className="h5 mb-0">Messages</h5>
                  </div>
                 <div className="header-message-list p-2">
                     <a className="dropdown-item" href="#">
                       <div className="d-flex align-items-center">
                          <img src="assets/images/avatars/avatar-1.png" alt="" className="rounded-circle" width="50" height="50" />
                          <div className="ms-3 flex-grow-1">
                            <h6 className="mb-0 dropdown-msg-user">Amelio Joly <span className="msg-time float-end text-secondary">1 m</span></h6>
                            <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">The standard chunk of lorem...</small>
                          </div>
                       </div>
                     </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                         <img src="assets/images/avatars/avatar-2.png" alt="" className="rounded-circle" width="50" height="50" />
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">Althea Cabardo <span className="msg-time float-end text-secondary">7 m</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">Many desktop publishing</small>
                         </div>
                      </div>
                    </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                         <img src="assets/images/avatars/avatar-3.png" alt="" className="rounded-circle" width="50" height="50" />
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">Katherine Pechon <span className="msg-time float-end text-secondary">2 h</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">Making this the first true</small>
                         </div>
                      </div>
                    </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                         <img src="assets/images/avatars/avatar-4.png" alt="" className="rounded-circle" width="50" height="50" />
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">Peter Costanzo <span className="msg-time float-end text-secondary">3 h</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">It was popularised in the 1960</small>
                         </div>
                      </div>
                    </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                         <img src="assets/images/avatars/avatar-5.png" alt="" className="rounded-circle" width="50" height="50" />
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">Thomas Wheeler <span className="msg-time float-end text-secondary">1 d</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">If you are going to use a passage</small>
                         </div>
                      </div>
                    </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                         <img src="assets/images/avatars/avatar-6.png" alt="" className="rounded-circle" width="50" height="50" />
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">Johnny Seitz <span className="msg-time float-end text-secondary">2 w</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">All the Lorem Ipsum generators</small>
                         </div>
                      </div>
                    </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                         <img src="assets/images/avatars/avatar-1.png" alt="" className="rounded-circle" width="50" height="50" />
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">Amelio Joly <span className="msg-time float-end text-secondary">1 m</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">The standard chunk of lorem...</small>
                         </div>
                      </div>
                    </a>
                   <a className="dropdown-item" href="#">
                     <div className="d-flex align-items-center">
                        <img src="assets/images/avatars/avatar-2.png" alt="" className="rounded-circle" width="50" height="50" />
                        <div className="ms-3 flex-grow-1">
                          <h6 className="mb-0 dropdown-msg-user">Althea Cabardo <span className="msg-time float-end text-secondary">7 m</span></h6>
                          <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">Many desktop publishing</small>
                        </div>
                     </div>
                   </a>
                   <a className="dropdown-item" href="#">
                     <div className="d-flex align-items-center">
                        <img src="assets/images/avatars/avatar-3.png" alt="" className="rounded-circle" width="50" height="50" />
                        <div className="ms-3 flex-grow-1">
                          <h6 className="mb-0 dropdown-msg-user">Katherine Pechon <span className="msg-time float-end text-secondary">2 h</span></h6>
                          <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">Making this the first true</small>
                        </div>
                     </div>
                   </a>
                </div>
                <div className="p-2">
                  <div><hr className="dropdown-divider" /></div>
                    <a className="dropdown-item" href="#">
                      <div className="text-center">View All Messages</div>
                    </a>
                </div>
               </div>
              </li>
              <li className="nav-item dropdown dropdown-large">
                <a className="nav-link dropdown-toggle dropdown-toggle-nocaret" href="#" data-bs-toggle="dropdown">
                  <div className="notifications">
                    <span className="notify-badge">8</span>
                    <i className="bi bi-bell-fill"></i>
                  </div>
                </a>
                <div className="dropdown-menu dropdown-menu-end p-0">
                  <div className="p-2 border-bottom m-2">
                      <h5 className="h5 mb-0">Notifications</h5>
                  </div>
                  <div className="header-notifications-list p-2">
                      <a className="dropdown-item" href="#">
                        <div className="d-flex align-items-center">
                           <div className="notification-box bg-light-primary text-primary"><i className="bi bi-basket2-fill"></i></div>
                           <div className="ms-3 flex-grow-1">
                             <h6 className="mb-0 dropdown-msg-user">New Orders <span className="msg-time float-end text-secondary">1 m</span></h6>
                             <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">You have recived new orders</small>
                           </div>
                        </div>
                      </a>
                     <a className="dropdown-item" href="#">
                       <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-purple text-purple"><i className="bi bi-people-fill"></i></div>
                          <div className="ms-3 flex-grow-1">
                            <h6 className="mb-0 dropdown-msg-user">New Customers <span className="msg-time float-end text-secondary">7 m</span></h6>
                            <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">5 new user registered</small>
                          </div>
                       </div>
                     </a>
                     <a className="dropdown-item" href="#">
                       <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-success text-success"><i className="bi bi-file-earmark-bar-graph-fill"></i></div>
                          <div className="ms-3 flex-grow-1">
                            <h6 className="mb-0 dropdown-msg-user">24 PDF File <span className="msg-time float-end text-secondary">2 h</span></h6>
                            <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">The pdf files generated</small>
                          </div>
                       </div>
                     </a>
                     <a className="dropdown-item" href="#">
                       <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-orange text-orange"><i className="bi bi-collection-play-fill"></i></div>
                          <div className="ms-3 flex-grow-1">
                            <h6 className="mb-0 dropdown-msg-user">Time Response  <span className="msg-time float-end text-secondary">3 h</span></h6>
                            <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">5.1 min avarage time response</small>
                          </div>
                       </div>
                     </a>
                     <a className="dropdown-item" href="#">
                       <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-info text-info"><i className="bi bi-cursor-fill"></i></div>
                          <div className="ms-3 flex-grow-1">
                            <h6 className="mb-0 dropdown-msg-user">New Product Approved  <span className="msg-time float-end text-secondary">1 d</span></h6>
                            <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">Your new product has approved</small>
                          </div>
                       </div>
                     </a>
                     <a className="dropdown-item" href="#">
                       <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-pink text-pink"><i className="bi bi-gift-fill"></i></div>
                          <div className="ms-3 flex-grow-1">
                            <h6 className="mb-0 dropdown-msg-user">New Comments <span className="msg-time float-end text-secondary">2 w</span></h6>
                            <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">New customer comments recived</small>
                          </div>
                       </div>
                     </a>
                     <a className="dropdown-item" href="#">
                       <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-warning text-warning"><i className="bi bi-droplet-fill"></i></div>
                          <div className="ms-3 flex-grow-1">
                            <h6 className="mb-0 dropdown-msg-user">New 24 authors<span className="msg-time float-end text-secondary">1 m</span></h6>
                            <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">24 new authors joined last week</small>
                          </div>
                       </div>
                     </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-primary text-primary"><i className="bi bi-mic-fill"></i></div>
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">Your item is shipped <span className="msg-time float-end text-secondary">7 m</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">Successfully shipped your item</small>
                         </div>
                      </div>
                    </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-success text-success"><i className="bi bi-lightbulb-fill"></i></div>
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">Defense Alerts <span className="msg-time float-end text-secondary">2 h</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">45% less alerts last 4 weeks</small>
                         </div>
                      </div>
                    </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-info text-info"><i className="bi bi-bookmark-heart-fill"></i></div>
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">4 New Sign Up <span className="msg-time float-end text-secondary">2 w</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">New 4 user registartions</small>
                         </div>
                      </div>
                    </a>
                    <a className="dropdown-item" href="#">
                      <div className="d-flex align-items-center">
                        <div className="notification-box bg-light-bronze text-bronze"><i className="bi bi-briefcase-fill"></i></div>
                         <div className="ms-3 flex-grow-1">
                           <h6 className="mb-0 dropdown-msg-user">All Documents Uploaded <span className="msg-time float-end text-secondary">1 mo</span></h6>
                           <small className="mb-0 dropdown-msg-text text-secondary d-flex align-items-center">Sussessfully uploaded all files</small>
                         </div>
                      </div>
                    </a>
                 </div>
                 <div className="p-2">
                   <div><hr className="dropdown-divider" /></div>
                     <a className="dropdown-item" href="#">
                       <div className="text-center">View All Notifications</div>
                     </a>
                 </div>
                </div>
              </li>
              </ul>
              </div>
              <div className="dropdown dropdown-user-setting">
                <a className="dropdown-toggle dropdown-toggle-nocaret" href="#" data-bs-toggle="dropdown">
                  <div className="user-setting d-flex align-items-center gap-3">
                    <img src="assets/images/avatars/avatar-1.png" className="user-img" alt="" />
                    <div className="d-none d-sm-block">
                       <p className="user-name mb-0">Jhon Deo</p>
                      <small className="mb-0 dropdown-user-designation">HR Manager</small>
                    </div>
                  </div>
                </a>
                <ul className="dropdown-menu dropdown-menu-end">
                   <li>
                      <a className="dropdown-item" href="pages-user-profile.html">
                         <div className="d-flex align-items-center">
                           <div className=""><i className="bi bi-person-fill"></i></div>
                           <div className="ms-3"><span>Profile</span></div>
                         </div>
                       </a>
                    </li>
                    <li>
                      <a className="dropdown-item" href="#">
                         <div className="d-flex align-items-center">
                           <div className=""><i className="bi bi-gear-fill"></i></div>
                           <div className="ms-3"><span>Setting</span></div>
                         </div>
                       </a>
                    </li>
                    <li>
                      <a className="dropdown-item" href="index2.html">
                         <div className="d-flex align-items-center">
                           <div className=""><i className="bi bi-speedometer"></i></div>
                           <div className="ms-3"><span>Dashboard</span></div>
                         </div>
                       </a>
                    </li>
                    <li>
                      <a className="dropdown-item" href="#">
                         <div className="d-flex align-items-center">
                           <div className=""><i className="bi bi-piggy-bank-fill"></i></div>
                           <div className="ms-3"><span>Earnings</span></div>
                         </div>
                       </a>
                    </li>
                    <li>
                      <a className="dropdown-item" href="#">
                         <div className="d-flex align-items-center">
                           <div className=""><i className="bi bi-cloud-arrow-down-fill"></i></div>
                           <div className="ms-3"><span>Downloads</span></div>
                         </div>
                       </a>
                    </li>
                    <li><hr className="dropdown-divider" /></li>
                    <li>
                      <a className="dropdown-item" href="authentication-signup-with-header-footer.html">
                         <div className="d-flex align-items-center">
                           <div className=""><i className="bi bi-lock-fill"></i></div>
                           <div className="ms-3"><span>Logout</span></div>
                         </div>
                       </a>
                    </li>
                </ul>
              </div>
        </nav>
      </header>
   </>
  )
}

export default Navbar