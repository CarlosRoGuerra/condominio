import React, { useState } from 'react';
import { useUser } from './hooks/useUser';
import { useTheme } from './hooks/useTheme';
import { FaUserCircle } from 'react-icons/fa';
import { MdDashboard, MdAccountCircle, MdSettings, MdLogout } from 'react-icons/md';

const Dashboard = () => {
  const { user } = useUser();
  const { theme, toggleTheme } = useTheme();

  return (
    <div className={`app ${theme === 'dark' ? 'dark' : ''}`}>
      <div className="flex h-screen">
        {/* Sidebar Navigation */}
        <div className="bg-gray-800 text-gray-100 p-4 flex flex-col justify-between">
          <div>
            <div className="flex items-center mb-6">
              {user.profilePhoto ? (
                <img src={user.profilePhoto} alt="Profile" className="w-12 h-12 rounded-full" />
              ) : (
                <div className="bg-gray-600 w-12 h-12 rounded-full flex items-center justify-center text-2xl font-bold">
                  {user.name.charAt(0).toUpperCase()}
                </div>
              )}
              <span className="ml-4 font-medium">{user.name}</span>
            </div>
            <nav>
              <ul className="space-y-2">
                <li>
                  <a href="#" className="flex items-center space-x-2 hover:bg-gray-700 px-3 py-2 rounded">
                    <MdDashboard />
                    <span>Dashboard</span>
                  </a>
                </li>
                <li>
                  <a href="#" className="flex items-center space-x-2 hover:bg-gray-700 px-3 py-2 rounded">
                    <MdAccountCircle />
                    <span>Profile</span>
                  </a>
                </li>
                <li>
                  <a href="#" className="flex items-center space-x-2 hover:bg-gray-700 px-3 py-2 rounded">
                    <MdSettings />
                    <span>Settings</span>
                  </a>
                </li>
              </ul>
            </nav>
          </div>
          <div>
            <button
              onClick={toggleTheme}
              className="flex items-center space-x-2 hover:bg-gray-700 px-3 py-2 rounded"
            >
              {theme === 'dark' ? <MdSunny /> : <MdMoonOutline />}
              <span>{theme === 'dark' ? 'Light Mode' : 'Dark Mode'}</span>
            </button>
            <a
              href="#"
              className="flex items-center space-x-2 hover:bg-gray-700 px-3 py-2 rounded mt-4"
            >
              <MdLogout />
              <span>Logout</span>
            </a>
          </div>
        </div>

        {/* Main Content */}
        <div className="flex-1 bg-gray-100 dark:bg-gray-800 p-6">
          <h1 className="text-2xl font-bold mb-4">Welcome to the Dashboard</h1>
          {/* Add your main dashboard content here */}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;