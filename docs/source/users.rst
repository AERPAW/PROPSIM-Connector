Users Document
######################
| This section is meant for users of the PCHEM Service, who are programmers and call PCHEM APIs within their python script to interact with Propsim. 

| **Examples**

| You can refer to and edit / build on ``sample_experiment.py`` within the ``examples`` directory.

| You can also call apis interactively, by running ``pchem_interactive``, located within the ``examples`` directory.

| **WorkFlow**

#. Import the client pchem module as follows: ``from pchem import client as pchem_client``

#. Open or edit an emulation file: Open a pre-loaded scenario file by calling the ``open_emulation(<filename>)``. You can also call ``edit_emulation(<filename>)`` if you want to change the center frequency or other parameters. 

#. Start the emulation: Call ``start_emulation()`` or ``start_emulation_after_edit()``.

#. Edit channel attenuation as desired, by calling ``set_output_gain(<channel_number>, <db_gain>)``, e.g. to replay recorded measurements or as per the position of radio nodes, controlled by another user-defined script.

#. Stop the emulation: Call ``close_emulation()``.

You can refer to the `APIs` section for a list of all implemented apis and to the `Developers` section to contribute new apis.

