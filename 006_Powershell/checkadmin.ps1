try{
    $check = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $Principle = New-Object Security.Principal.WindowsPrincipal ($check)
    $is_admin = $Principle.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)
    if($is_admin){
        "You have the admin previlage"
    }
    else{
        "you dont have admin"
    }
}
catch{
    "error in line number $($_.InvocationInfo.ScriptLineNumber) : $($Error[0])"

}