import React from 'react'

export const sidebar = {
  chat: {
    label: 'Chat',
  },
  menus: {
    label: 'Menus',
    items: [
      { name: 'Menu 1', href: '#' },
      { name: 'Menu 2', href: '#' },
      { name: 'Menu 3', href: '#' },
    ],
  },
  account: {
    label: 'Account',
    loginOption: 'Log in',
  },
}

const a = 'a'

const Sidebar = () => {
  return (
    <div>
      <div>MVC Logo</div>
      <div>{sidebar.chat.label}</div>
      <div>
        <label>{sidebar.menus.label}</label>
        <ul>
          {sidebar.menus.items.map((item, i) => (
            <li key={i}> {item.name}</li>
          ))}
        </ul>
      </div>
      <div>
        {sidebar.account.label}
        {sidebar.account.loginOption}
      </div>
    </div>
  )
}

export default Sidebar
