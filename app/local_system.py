import logging
import platform
import subprocess

logger = logging.getLogger(__name__)


class Error(Exception):
    pass


class ShutdownError(Error):
    pass

class DutShutdownError(Error):
    pass

class DutRestartError(Error):
    pass

def hostname():
    return platform.node()


def shutdown():
    logger.info('Shutting down system')
    return _exec_shutdown(restart=True)


def restart():
    logger.info('Rebooting system')
    return _exec_shutdown(restart=True)

def dut_shutdown():
    logger.info('Shutting down attached system')
    return _exec_dut_shutdown()

def dut_restart():
    logger.info('Restarting attached system')
    return _exec_dut_restart()

def _exec_shutdown(restart):
    if restart:
        param = '--reboot'
    else:
        param = '--poweroff'

    result = subprocess.run(['sudo', '/sbin/shutdown', param, 'now'],
                            capture_output=True,
                            text=True)
    if 'failed' in result.stderr.lower():
        raise ShutdownError(result.stdout + result.stderr)
    else:
        if result.stdout:
            logger.info(result.stdout)
        if result.stderr:
            logger.info(result.stderr)
    return True

def _exec_dut_shutdown():
    #result = subprocess.run(['./system_scripts/', 'power_hit.py'], capture_output=True, text=True)
    result = subprocess.run(['python3', 'system_scripts/power_hit.py'], capture_output=True, text=True)
    #result = subprocess.run(['whoami'], capture_output=True, text=True)
    #result = subprocess.run(['pwd'], capture_output=True, text=True)
    if 'failed' in result.stderr.lower():
        raise DutShutdownError(result.stdout + result.stderr)
    else:
        if result.stdout:
            logger.info(result.stdout)
        if result.stderr:
            logger.info(result.stderr)
    return True

def _exec_dut_restart():
    #result = subprocess.run(['./system_scripts/', 'reset_hit.py'], capture_output=True, text=True)
    result = subprocess.run(['python3', 'system_scripts/reset_hit.py'], capture_output=True, text=True)
    #result = subprocess.run(['whoami'], capture_output=True, text=True)
    #result = subprocess.run(['pwd'], capture_output=True, text=True)
    if 'failed' in result.stderr.lower():
        raise DutRestartError(result.stdout + result.stderr)
    else:
        if result.stdout:
            logger.info(result.stdout)
        if result.stderr:
            logger.info(result.stderr)
    return True

