User Manual
===========

This page contains information on how to install, update, and use the Unreal Bot tool. 

Install
-------

Update
------

Usage
-----

-s, --setup
^^^^^^^^^^^

.. code-block:: console

   unrealbot -s dependencies.json

Example dependencies.json file:

.. code-block:: json

   {
    "version": 1.0,
    "Package0" : {
        "Repository" : "nuget-hosted",
        "Format" : "nuget",
        "ComponentName" : "AssetFactory.SFX.Ambient.Dark.Hostile",
        "ComponentVersion" : "1.0.0",
        "UnpackPath" : "./AssetFactory/Content/AssetFactory/SFX/Ambient/Dark"
        }
    }