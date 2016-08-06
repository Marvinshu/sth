$('.list-view').each(->
    id = $(this).attr('id')
    Sortable.create(document.getElementById(id), {
        group: "list-view"
        animation: 150
        ghostClass: "ghost"  #  Class name for the drop placeholder
        chosenClass: "chosen"  #  Class name for the chosen item
        filter: ".undrag"

        onUpdate: (event)->
            console.log event

        onAdd: (event)->
            console.log event
    })
)


$.app.controller('TaskCtrl', ($scope)->
    $scope.o = {
        todo: null
        doing: null
        done: null
    }
    $scope.todo = {
        title: ''
        type: 1
    }

    $scope.edit = false

    $scope.insert = (type)->
        $scope.edit = true
        setTimeout(->
            $("#text-#{type}").focus()
        , 100)
        false
    
    $scope.cancel_add = (type)->
        $scope.edit = false

    $scope.add = ()->
        $.only_ajax({
            method: 'POST'
            url: '/j/task'
            data: $scope.todo
            success: ->
                $.only_ajax({
                    url: "/j/task/list?type=1",
                    success: (r)->
                        v = angular.element($("[ng-controller=TaskCtrl]")).scope()
                        v.o.todo = r.data
                        v.$apply()
                })

        })

        false

)


$.only_ajax({
    url: "/j/task/list?type=1",
    success: (r)->
        v = angular.element($("[ng-controller=TaskCtrl]")).scope()
        v.o.todo = r.data
        v.$apply()
})

$.only_ajax({
    url: "/j/task/list?type=2",
    success: (r)->
        v = angular.element($("[ng-controller=TaskCtrl]")).scope()
        v.o.doing = r.data
        v.$apply()
})

$.only_ajax({
    url: "/j/task/list?type=3",
    success: (r)->
        v = angular.element($("[ng-controller=TaskCtrl]")).scope()
        v.o.done = r.data
        v.$apply()
})


