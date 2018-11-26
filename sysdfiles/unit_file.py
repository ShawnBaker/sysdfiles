from .ini_file import IniFile


# =============================================================================
# UnitFile
# =============================================================================
class UnitFile(IniFile):

    def __init__(self, file_name):
        IniFile.__init__(self, file_name)
        self.add_properties('unit',
                            [['after', 'l'],
                             ['allow_isolate', 'b'],
                             ['assert_ac_power', 'b'],
                             ['assert_architecture'],
                             ['assert_capability'],
                             ['assert_control_group_controller'],
                             ['assert_directory_not_empty'],
                             ['assert_file_not_empty'],
                             ['assert_file_is_executable'],
                             ['assert_first_boot', 'b'],
                             ['assert_group'],
                             ['assert_host'],
                             ['assert_kernel_command_line'],
                             ['assert_kernel_version'],
                             ['assert_needs_update'],
                             ['assert_path_exists'],
                             ['assert_path_exists_glob'],
                             ['assert_path_is_directory'],
                             ['assert_path_is_mount_point'],
                             ['assert_path_is_read_write'],
                             ['assert_path_is_symbolic_link'],
                             ['assert_security'],
                             ['assert_virtualization'],
                             ['assert_user'],
                             ['before', 'l'],
                             ['binds_to', 'l'],
                             ['collect_mode'],
                             ['condition_ac_power', 'b'],
                             ['condition_architecture'],
                             ['condition_capability'],
                             ['condition_control_group_controller'],
                             ['condition_directory_not_empty'],
                             ['condition_file_is_executable'],
                             ['condition_file_not_empty'],
                             ['condition_first_boot', 'b'],
                             ['condition_group'],
                             ['condition_host'],
                             ['condition_kernel_command_line'],
                             ['condition_kernel_version'],
                             ['condition_needs_update'],
                             ['condition_path_exists'],
                             ['condition_path_exists_glob'],
                             ['condition_path_is_directory'],
                             ['condition_path_is_mount_point'],
                             ['condition_path_is_symbolic_link'],
                             ['condition_path_is_read_write'],
                             ['condition_security'],
                             ['condition_user'],
                             ['condition_virtualization'],
                             ['conflicts', 'l'],
                             ['default_dependencies', 'b'],
                             ['description'],
                             ['documentation', 'l'],
                             ['failure_action'],
                             ['ignore_on_isolate', 'b'],
                             ['job_running_timeout_sec', 'ns'],
                             ['job_timeout_sec', 'ns'],
                             ['job_timeout_action'],
                             ['job_timeout_reboot_argument'],
                             ['joins_namespace_of', 'l'],
                             ['on_failure', 'l'],
                             ['on_failure_job_mode'],
                             ['part_of', 'l'],
                             ['propagates_reload_to', 'l'],
                             ['reboot_argument'],
                             ['refuse_manual_start', 'b'],
                             ['refuse_manual_stop', 'b'],
                             ['reload_propagated_from', 'l'],
                             ['requires', 'l'],
                             ['requires_mounts_for', 'l'],
                             ['requisite', 'l'],
                             ['source_path'],
                             ['start_limit_action'],
                             ['start_limit_burst', 'i'],
                             ['start_limit_interval_sec', 'ns'],
                             ['stop_when_unneeded', 'b'],
                             ['success_action'],
                             ['wants', 'l']])
        self.add_properties('install',
                            [['alias', 'l'],
                             ['also', 'l'],
                             ['default_instance'],
                             ['required_by', 'l'],
                             ['wanted_by', 'l']])

    # =========================================================================
    # add_exec_properties
    # =========================================================================
    def add_exec_properties(self, section_name=''):
        if not section_name:
            section_name = type(self).__name__
            if section_name.endswith('File'):
                section_name = section_name[:-4]
        self.add_properties(section_name,
                            [['ambient_capabilities', 'l'],
                             ['app_armor_profile'],
                             ['bind_paths', 'l'],
                             ['bind_read_only_paths', 'l'],
                             ['cache_directory', 'l'],
                             ['cache_directory_mode'],
                             ['capability_bounding_set', 'l'],
                             ['configuration_directory', 'l'],
                             ['configuration_directory_mode'],
                             ['cpu_affinity', 'l'],
                             ['cpu_scheduling_policy'],
                             ['cpu_scheduling_priority', 'i'],
                             ['cpu_scheduling_reset_on_fork', 'b'],
                             ['dynamic_user', 'b'],
                             ['environment', 'l'],
                             ['environment_file', 'l', ' ', 1],
                             ['group'],
                             ['ignore_sig_pipe', 'b'],
                             ['inaccessible_paths', 'l'],
                             ['io_scheduling_class', 'i'],
                             ['io_scheduling_priority', 'i'],
                             ['keyring_mode'],
                             ['limit_as'],
                             ['limit_core'],
                             ['limit_cpu'],
                             ['limit_data'],
                             ['limit_fsize'],
                             ['limit_locks'],
                             ['limit_mem_lock'],
                             ['limit_msg_queue'],
                             ['limit_nice'],
                             ['limit_no_file'],
                             ['limit_nproc'],
                             ['limit_rss'],
                             ['limit_rt_prio'],
                             ['limit_rt_time'],
                             ['limit_sig_pending'],
                             ['limit_stack'],
                             ['lock_personality', 'b'],
                             ['log_extra_fields', 'l'],
                             ['log_level_max'],
                             ['logs_directory', 'l'],
                             ['logs_directory_mode'],
                             ['memory_deny_write_execute', 'b'],
                             ['mount_api_vfs', 'b'],
                             ['mount_flags'],
                             ['nice', 'i'],
                             ['no_new_privileges', 'b'],
                             ['oom_score_adjust', 'i'],
                             ['pam_name'],
                             ['pass_environment', 'l'],
                             ['personality'],
                             ['private_devices', 'b'],
                             ['private_mounts', 'b'],
                             ['private_network', 'b'],
                             ['private_tmp', 'b'],
                             ['private_users', 'b'],
                             ['protect_control_groups', 'b'],
                             ['protect_home'],
                             ['protect_kernel_modules', 'b'],
                             ['protect_kernel_tunables', 'b'],
                             ['protect_system'],
                             ['read_only_paths', 'l'],
                             ['read_write_paths', 'l'],
                             ['remove_ipc', 'b'],
                             ['restrict_address_families', 'l'],
                             ['restrict_namespaces'],
                             ['restrict_realtime', 'b'],
                             ['root_directory'],
                             ['root_image'],
                             ['runtime_directory', 'l'],
                             ['runtime_directory_mode'],
                             ['runtime_directory_preserve'],
                             ['se_linux_context'],
                             ['secure_bits', 'l'],
                             ['smack_process_label'],
                             ['standard_error'],
                             ['standard_input'],
                             ['standard_input_data'],
                             ['standard_input_text'],
                             ['standard_output'],
                             ['state_directory', 'l'],
                             ['state_directory_mode'],
                             ['supplementary_groups', 'l'],
                             ['syslog_facility'],
                             ['syslog_identifier'],
                             ['syslog_level'],
                             ['syslog_level_prefix', 'b'],
                             ['system_call_architectures', 'l'],
                             ['system_call_error_number', 'i'],
                             ['system_call_filter', 'l'],
                             ['temporary_file_system', 'l'],
                             ['timer_slack_nsec', 'ns'],
                             ['tty_path'],
                             ['tty_reset', 'b'],
                             ['tty_vhangup', 'b'],
                             ['tty_vt_disallocate', 'b'],
                             ['umask'],
                             ['unset_environment', 'l'],
                             ['user'],
                             ['utmp_identifier'],
                             ['utmp_mode'],
                             ['working_directory']])

    # =========================================================================
    # add_kill_properties
    # =========================================================================
    def add_kill_properties(self, section_name=''):
        if not section_name:
            section_name = type(self).__name__
            if section_name.endswith('File'):
                section_name = section_name[:-4]
        self.add_properties(section_name,
                            [['kill_mode'],
                             ['kill_signal'],
                             ['send_sighup', 'b'],
                             ['send_sigkill', 'b']])

    # =========================================================================
    # add_resource_control_properties
    # =========================================================================
    def add_resource_control_properties(self, section_name=''):
        if not section_name:
            section_name = type(self).__name__
            if section_name.endswith('File'):
                section_name = section_name[:-4]
        self.add_properties(section_name,
                            [['block_io_accounting', 'b'],
                             ['block_io_device_weight', 'i'],
                             ['block_io_read_bandwidth', 'nb'],
                             ['block_io_weight', 'i'],
                             ['block_io_write_bandwidth', 'nb'],
                             ['cpu_accounting', 'b'],
                             ['cpu_quota'],
                             ['cpu_shares', 'i'],
                             ['cpu_weight', 'i'],
                             ['delegate'],
                             ['device_allow'],
                             ['device_policy'],
                             ['io_accounting', 'b'],
                             ['io_device_weight', 'i'],
                             ['io_read_bandwidth_max', 'nb'],
                             ['io_read_io_ps_max', 'nb'],
                             ['io_weight', 'i'],
                             ['io_write_bandwidth_max', 'nb'],
                             ['io_write_io_ps_max', 'nb'],
                             ['ip_accounting', 'b'],
                             ['ip_address_allow', 'l'],
                             ['ip_address_deny', 'l'],
                             ['memory_accounting', 'b'],
                             ['memory_high', 'nb'],
                             ['memory_limit', 'nb'],
                             ['memory_low', 'nb'],
                             ['memory_max', 'nb'],
                             ['memory_swap_max', 'nb'],
                             ['slice'],
                             ['startup_block_io_weight', 'i'],
                             ['startup_cpu_shares', 'i'],
                             ['startup_cpu_weight', 'i'],
                             ['startup_io_weight', 'i'],
                             ['tasks_accounting', 'b'],
                             ['tasks_max']])
