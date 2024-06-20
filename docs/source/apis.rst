API Definitions
###########################

**API Response Format**
| To-do

**System Information APIs**

``get_identity()``
   | Returns the following Propsim information: Company Name, Device Name, Serial Number, Firmware Version Number 
   |
   | `Example`: 

``get_version()``
   | Returns the standard commands for programmable instuments (SCPI) version of Propsim. The response should be 1999.0.
   |
   | `Example`:

**Emulation APIs**

``open_emulation(<filename>)``
    | Opens the emulation defined in ``<filename>``. The folder name separater within <filename> should be duplicated, e.g. "D:\\User Emulations\\Anil\\srsran_4g_siso.smu".
    | This api is, in most cases, followed by a call to start_emulation() to run the emulation.
    |
    | `Example`:

``edit_emulation(<filename>)``
    | Opens the emulation defined in ``<filename>`` in editing mode. This allows the user to change emulation settings before loading the emulation to hardware. A typical use case is to open an emulation in edit mode, change the center frequency, and then load the emulation to hardware.
    | This api is, in most cases, followed by a call to start_emulation_after_edit() to run the emulation.
    |
    | `Example`:

``start_emulation_after_edit()``
    | Runs an emulation that has been opened in edit mode.
    |
    | `Example`:

``start_emulation()``
    | Runs an emulation that was not opened in edit mode. 
    |
    | `Example`:

``pause_emulation()``
    | Pauses a running emulation, without rewinding to the start of the emulation.
    |
    | `Example`:

``resume_emulation()``
    | Contines a paused emulation.
    |
    | `Example`:

``close_emulation()``
    | Closes an open emulation.
    |
    | `Example`:

.. ``step_emulation()``
..     Not implemented.

**Channel APIs**

``set_ouput_gain(<channel_number>, <output_gain>)``
    | Sets the output gain of the channel, corresponding to the provided ``<channel_number>``, to the provided ``<output_gain>`` value, in dB.
    |
    | Example:

.. ``set_output_phase_deg()``

.. **Channel Input APIs**

.. ``set_avg_input_level()``

.. ``set_input_phase_deg()``

.. ``set_input_gain()``

.. ``set_input_loss()``

.. **Channel Output APIs**

.. ``set_ouput_gain()``

.. ``set_output_phase_deg()``

.. ``set_average_output_level()``
